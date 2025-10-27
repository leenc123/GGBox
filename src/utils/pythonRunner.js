import { spawn } from 'child_process';
import path from 'path';
export class PythonRunner {
  constructor() {
    this.pythonPath = this.getPythonPath();
    this.scriptPath = path.join(process.cwd(), 'scripts', 'crawler.py');
  }
  getPythonPath() {
    // 根据系统选择 Python 命令
    if (process.platform === 'win32') {
      return 'python';
    } else {
      return 'python3';
    }
  }
  async runCrawler(url, selector = null) {
    console.log(333333333333)
    return new Promise((resolve, reject) => {
      const args = [this.scriptPath, url];
      if (selector) {
        args.push(selector);
      }
      console.log('执行 Python 命令:', this.pythonPath, args);
      const pythonProcess = spawn(this.pythonPath, args, {
        cwd: process.cwd(),
        stdio: ['pipe', 'pipe', 'pipe']
      });
      let data = '';
      let errorData = '';
      pythonProcess.stdout.on('data', (chunk) => {
        data += chunk.toString();
      });
      pythonProcess.stderr.on('data', (chunk) => {
        errorData += chunk.toString();
        console.error('Python stderr:', chunk.toString());
      });
      pythonProcess.on('close', (code) => {
        if (code === 0) {
          try {
            const result = JSON.parse(data);
            resolve(result);
          } catch (parseError) {
            reject(`JSON 解析错误: ${parseError.message}, 原始数据: ${data}`);
          }
        } else {
          reject(`Python 进程退出码: ${code}, 错误: ${errorData}`);
        }
      });
      pythonProcess.on('error', (error) => {
        reject(`启动 Python 进程失败: ${error.message}`);
      });
      // 设置超时
      setTimeout(() => {
        pythonProcess.kill();
        reject('Python 进程执行超时');
      }, 30000); // 30秒超时
    });
  }
}