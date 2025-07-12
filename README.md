# CoreSky 自动化任务脚本

这是一个针对 CoreSky 平台的自动化签到和任务执行脚本，支持多账户批量操作，集成了验证码识别、代理切换等功能。

## 🌟 功能特性

- ✅ **自动签到**: 支持 CoreSky 平台的每日签到任务
- 🔐 **钱包签名**: 使用以太坊私钥进行消息签名认证
- 🤖 **验证码识别**: 集成 ddddocr 自动识别滑块验证码
- 🌍 **代理支持**: 支持使用代理进行请求，避免IP限制
- 📊 **批量处理**: 支持从 Excel 文件批量导入账户信息
- 🔄 **自动重试**: 内置重试机制，提高任务成功率
- 📈 **投票功能**: 自动使用账户积分进行投票
- 📝 **进度跟踪**: 自动记录已完成的账户，避免重复执行

## 📋 环境要求

- Python 3.7+
- 以下 Python 包:
  ```
  requests
  pycryptodome
  ddddocr
  eth-account
  openpyxl
  loguru
  ```

## 🛠️ 安装指南

1. **克隆项目**
   ```bash
   git clone https://github.com/cyptoKris/coresky_task.git
   cd coresky_task
   ```

2. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

3. **配置代理（推荐）**
   
   为了避免IP限制和提高成功率，强烈建议使用动态代理服务。推荐使用 [Kookeey 代理服务](https://www.kookeey.com/?aff=23304422)，提供稳定的动态IP代理。

   在 `src/coresky_daily.py` 文件中配置代理：
   ```python
   proxy = {
       'http': 'http://username:password@proxy-host:port',
       'https': 'http://username:password@proxy-host:port'
   }
   ```

4. **准备账户文件**
   
   使用提供的 `模版.xlsx` 文件，填入您的账户信息：
   - 列A: 序号
   - 列B: 钱包地址
   - 列C: 私钥

## 🚀 使用方法

### 基础使用

1. **配置账户信息**
   
   编辑 `模版.xlsx` 文件，添加您的钱包地址和私钥信息。

2. **运行脚本**
   ```bash
   python src/coresky_daily.py
   ```

3. **查看结果**
   
   脚本会自动执行以下任务：
   - 登录验证
   - 完成每日签到
   - 自动投票
   - 记录完成状态

### 高级配置

#### 代理配置
```python
# 在 src/coresky_daily.py 中修改代理设置
proxy = {
    'http': 'http://your-proxy-host:port',
    'https': 'http://your-proxy-host:port'
}
```

#### 重试次数配置
```python
# 修改最大重试次数
MAX_RETRIES = 3
```

## 📁 文件结构

```
coresky_task/
├── src/                 # 源代码目录
│   ├── coresky_daily.py # 主要的自动化脚本
│   ├── ocr.py          # OCR相关工具类
│   └── __init__.py     # Python包初始化文件
├── requirements.txt     # 项目依赖
├── .gitignore          # Git忽略文件
├── 模版.xlsx            # 账户信息模板文件
├── 完成的账户id.txt      # 记录已完成任务的账户
├── LICENSE             # 开源协议
└── README.md           # 项目说明文档
```

## 🔧 核心功能详解

### 1. 账户管理
- 支持从 Excel 文件批量导入账户
- 自动生成账户ID（地址前6位）
- 记录已完成任务的账户，避免重复执行

### 2. 验证码处理
- 自动获取滑块验证码图片
- 使用 ddddocr 库进行图像识别
- 自动计算滑块位置并提交验证

### 3. 安全认证
- 使用以太坊私钥进行消息签名
- 支持 EIP-191 标准的消息签名
- 自动处理地址校验和格式

### 4. 任务执行
- 自动检查每日签到状态
- 智能跳过已完成的任务
- 自动使用积分进行投票

## ⚠️ 注意事项

1. **私钥安全**: 请妥善保管您的私钥，不要分享给他人
2. **代理使用**: 建议使用稳定的代理服务，避免IP被限制
3. **合规使用**: 请确保使用本脚本符合相关平台的服务条款
4. **备份数据**: 请定期备份您的账户文件和配置

## 🔗 推荐服务

### 代理服务
- [Kookeey 动态代理](https://www.kookeey.com/?aff=23304422) - 提供稳定的动态IP代理服务，适合自动化任务使用

## 📝 更新日志

- **v1.0.0**: 初始版本，支持基础的签到和投票功能
- 集成验证码自动识别
- 添加代理支持
- 完善错误处理和重试机制

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request 来改进这个项目。

## 📄 免责声明

本脚本仅供学习和研究使用，使用者需要自行承担使用风险。请确保您的使用行为符合相关法律法规和平台服务条款。

## 📞 支持

如果您在使用过程中遇到问题，请：
1. 检查配置文件是否正确
2. 确认网络连接和代理设置
3. 查看错误日志信息
4. 提交 Issue 描述问题详情

---

**Happy Coding! 🎉**