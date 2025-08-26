#!/usr/bin/env python3
"""
MCP Client Test Tool
Used to test connection to MCP server
"""
import asyncio
import json
import logging
import sys
from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def test_mcp_connection():
    """Test MCP server connection"""
    logger.info("Starting MCP server connection test...")
    
    try:
        # Start MCP server process
        server_params = StdioServerParameters(
            command=sys.executable,
            args=["main.py"]
        )
        
        logger.info(f"Starting MCP server with parameters: command={server_params.command}, args={server_params.args}")
        
        # Create stdio client connection
        async with stdio_client(server_params) as (read, write):
            logger.info("✓ Successfully created stdio connection")
            
            # Create client session
            async with ClientSession(read, write) as session:
                logger.info("✓ Successfully created client session")
                
                # Initialize session
                result = await session.initialize()
                logger.info("✓ Successfully initialized MCP session")
                logger.info(f"Server info: {result}")
                
                # Get server info from initialize result
                server_info = getattr(result, 'serverInfo', None)
                if server_info:
                    server_name = getattr(server_info, 'name', 'Unknown')
                else:
                    server_name = 'Unknown'
                logger.info(f"✓ Server name: {server_name}")
                
                # List available tools
                logger.info("Getting available tools list...")
                tools_response = await session.list_tools()
                logger.info(f"✓ Available tools count: {len(tools_response.tools)}")
                
                for tool in tools_response.tools:
                    logger.info(f"  - Tool name: {tool.name}")
                    logger.info(f"    Description: {tool.description}")
                    logger.info(f"    Input schema: {json.dumps(tool.inputSchema, indent=2)}")
                
                # Test tool call
                logger.info("Testing code analysis tool...")
                test_code = """
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
"""
                
                call_result = await session.call_tool("code_analysis", {"code": test_code})
                logger.info("✓ Tool call successful")
                
                # Extract text content from result
                if call_result.content:
                    for content in call_result.content:
                        if hasattr(content, 'text'):
                            logger.info(f"Analysis result: {content.text}")
                        else:
                            logger.info(f"Analysis result: {content}")
                else:
                    logger.info("No content in result")
                
                logger.info("🎉 MCP server connection test successful!")
                
    except Exception as e:
        logger.error(f"❌ MCP server connection test failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

async def main():
    """Main function"""
    logger.info("Starting MCP client test...")
    
    success = await test_mcp_connection()
    
    if success:
        logger.info("✓ All tests passed")
        sys.exit(0)
    else:
        logger.error("❌ Tests failed")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())