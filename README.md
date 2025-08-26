# Code MCP Server

一个基于Model Context Protocol (MCP)的代码管理服务器。

## 功能特性

- MCP协议支持
- 代码分析和处理
- RESTful API接口
- 异步处理能力

## 技术栈

- Python 3.11+
- FastAPI
- MCP (Model Context Protocol)
- Pydantic
- Uvicorn

## 开发环境

```bash
# 创建虚拟环境
uv venv

# 激活虚拟环境
source .venv/bin/activate

# 安装依赖
uv pip install -e .

# 安装开发依赖
uv pip install -e ".[dev]"
```

## 运行

```bash
# 启动服务器
python -m code_mcp_server.main
```

## 许可证

MIT License
