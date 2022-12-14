import os
import re
import subprocess
import asyncio


class Server:
    def __init__(self):
        self.process = None
    
    def start(self, jar_dir_pass):
        yield "Server starting up..."

        os.chdir(jar_dir_pass)

        yield "up .minecraft_server starting..."
        self.process = subprocess.Popen(
            ["java","-Xmx1024M","-Xms1024M","-jar","server-v1.19.jar","nogui"],
            text=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

        # ここのディレクトリに戻す
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        # await asyncio.sleep(5)

        while self.process.poll() is None:
            stdout_byte = self.process.stdout.readline().strip("\n")
            # stdout_text = stdout_byte.decode().strip()
            yield f"status: {self.process.poll()} {stdout_byte}"

            # 起動完了，コマンド自体は終了していない
            if("Done" in stdout_byte):
                break

        # ループを抜けた理由が無事に起動完了した
        if self.process.poll() is None:
            yield "start up"
            return

        yield 'start up error. kill proccess'
        self.process.kill()
        for log in self.getProccessCommunicateOutErr():
            yield log
        
    
    def stop(self):
        if self.process is None:
            yield "maybe server is not starting"
            return

        if self.process.poll() is not None:
            yield "already server is stopping"
            return

        yield "Server is stopping..."
        for log in self.getProccessCommunicateOutErr("stop", timeout=20):
            yield log
    
    def getHelp(self):
        print(self.process.stdin)
        self.process.stdin.write("help\n")
        self.process.stdin.flush()

        while True:
            line = self.process.stdout.readline().strip("\n")
            
            if not line or line == '' or self.process.poll() is not None:
                break

            yield line

            if "whitelist" in line:
                break

    def getJoinLog(self):
        self.process.stdin.write("list\n")
        self.process.stdin.flush()
        return self.process.stdout.readline().strip("\n")
    
    def getJoinNumber(self):
        join_log = self.getJoinLog()
        # 2番目にログイン人数が入る
        pattern = "(\[.*\]\s\[.*\]:\D*)(\d*)(.*)"
        join_number = re.match(pattern, join_log).group(2)
        return join_number



    def getProccessCommunicateOutErr(self, byte_input="", timeout=0):
        try:
            outs, errs = self.process.communicate(input=byte_input, timeout=timeout)
            
            yield "output log"
            yield outs
            
            # yield "error"
            # yield errs
        
        except subprocess.TimeoutExpired:
            self.process.kill()
            outs, errs = self.process.communicate()

            # yield "output"
            # yield outs
            
            yield "error log"
            yield errs