"""
MCP服务器主入口模块
"""
import asyncio
import logging
from .server import MCPServer

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def main():
    """主函数"""
    logger.info("启动Code MCP Server...")
    
    # 创建MCP服务器实例
    server = MCPServer()
    
    # 启动服务器
    await server.start()

if __name__ == "__main__":
    asyncio.run(main())
