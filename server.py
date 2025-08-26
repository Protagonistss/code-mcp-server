"""
MCP服务器核心实现
"""
import asyncio
import json
import logging
import sys
from typing import Any, Dict, List
from mcp import ServerSession
from mcp.server import Server
from mcp.server.stdio import stdio_server
from tools.code_analysis import CodeAnalysisTool

logger = logging.getLogger(__name__)

class MCPServer:
    """MCP服务器核心类"""
    
    def __init__(self):
        """初始化MCP服务器"""
        logger.info("初始化MCP服务器...")
        self.mcp_server = Server("code-mcp-server")
        self.tools = {
            "code_analysis": CodeAnalysisTool()
        }
        logger.info(f"注册工具: {list(self.tools.keys())}")
        self._setup_handlers()
        logger.info("MCP服务器初始化完成")
    
    def _setup_handlers(self):
        """设置MCP服务器处理器"""
        
        @self.mcp_server.list_tools()
        async def list_tools() -> List[Dict[str, Any]]:
            """列出可用的工具"""
            logger.info("收到工具列表请求")
            tools_list = [
                {
                    "name": "code_analysis",
                    "description": "分析代码结构和复杂度",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "code": {
                                "type": "string",
                                "description": "要分析的代码内容"
                            }
                        },
                        "required": ["code"]
                    }
                }
            ]
            logger.info(f"返回工具列表: {tools_list}")
            return tools_list
        
        @self.mcp_server.call_tool()
        async def call_tool(name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
            """调用指定的工具"""
            logger.info(f"调用工具: {name}, 参数: {arguments}")
            
            if name == "code_analysis":
                code = arguments.get("code", "")
                if not code:
                    raise ValueError("代码内容不能为空")
                
                result = await self.tools["code_analysis"].analyze(code)
                return {"result": result}
            
            raise ValueError(f"未知的工具: {name}")
    
    async def start(self):
        """启动MCP服务器"""
        logger.info("MCP服务器启动中...")
        
        try:
            async with stdio_server() as (read_stream, write_stream):
                async with ServerSession(self.mcp_server, read_stream, write_stream):
                    logger.info("MCP服务器已启动，等待连接...")
                    await asyncio.Future()  # 保持运行
        except Exception as e:
            logger.error(f"MCP服务器启动失败: {e}")
            sys.exit(1)
