"""
MCP服务器核心实现
"""
import logging
from mcp.server.fastmcp import FastMCP
from tools.code_analysis import CodeAnalysisTool

logger = logging.getLogger(__name__)

# 创建FastMCP服务器实例
mcp = FastMCP("code-mcp-server")

# 初始化代码分析工具
code_tool = CodeAnalysisTool()

@mcp.tool()
async def code_analysis(code: str) -> dict:
    """分析代码结构和复杂度
    
    Args:
        code: 要分析的代码内容
        
    Returns:
        代码分析结果
    """
    logger.info(f"🔍 收到代码分析请求，代码长度: {len(code)} 字符")
    
    if not code.strip():
        return {"error": "代码内容不能为空"}
    
    try:
        result = await code_tool.analyze(code)
        logger.info("✅ 代码分析完成")
        return result
    except Exception as e:
        logger.error(f"❌ 代码分析失败: {e}")
        return {"error": f"分析失败: {str(e)}"}

class MCPServer:
    """MCP服务器核心类（保持兼容性）"""
    
    def __init__(self):
        """初始化MCP服务器"""
        logger.info("初始化MCP服务器...")
        logger.info("注册工具: ['code_analysis']")
        logger.info("MCP服务器初始化完成")
    
    async def start(self):
        """启动MCP服务器"""
        logger.info("MCP服务器启动中...")
        logger.info("🚀 MCP服务器已启动，等待客户端连接...")
        
        # 使用FastMCP的异步方法启动服务器
        await mcp.run_stdio_async()
