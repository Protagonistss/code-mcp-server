"""
代码分析工具
"""
import ast
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class CodeAnalysisTool:
    """代码分析工具类"""
    
    async def analyze(self, code: str) -> Dict[str, Any]:
        """
        分析代码结构和复杂度
        
        Args:
            code: 要分析的代码内容
            
        Returns:
            分析结果字典
        """
        try:
            logger.info(f"开始分析代码，长度: {len(code)} 字符")
            
            # 基础统计
            stats = self._basic_stats(code)
            
            # 语法分析
            syntax_info = self._syntax_analysis(code)
            
            # 复杂度分析
            complexity = self._complexity_analysis(code)
            
            result = {
                "basic_stats": stats,
                "syntax_info": syntax_info,
                "complexity": complexity,
                "status": "success"
            }
            
            logger.info("代码分析完成")
            return result
            
        except Exception as e:
            logger.error(f"代码分析失败: {e}")
            return {
                "status": "error",
                "error": str(e)
            }
    
    def _basic_stats(self, code: str) -> Dict[str, Any]:
        """基础统计信息"""
        lines = code.split('\n')
        return {
            "total_lines": len(lines),
            "total_characters": len(code),
            "non_empty_lines": len([line for line in lines if line.strip()]),
            "empty_lines": len([line for line in lines if not line.strip()])
        }
    
    def _syntax_analysis(self, code: str) -> Dict[str, Any]:
        """语法分析"""
        try:
            tree = ast.parse(code)
            
            # 统计不同类型的节点
            node_counts = {}
            for node in ast.walk(tree):
                node_type = type(node).__name__
                node_counts[node_type] = node_counts.get(node_type, 0) + 1
            
            return {
                "syntax_valid": True,
                "node_counts": node_counts,
                "total_nodes": sum(node_counts.values())
            }
        except SyntaxError as e:
            return {
                "syntax_valid": False,
                "error": str(e),
                "line": e.lineno,
                "column": e.offset
            }
    
    def _complexity_analysis(self, code: str) -> Dict[str, Any]:
        """复杂度分析"""
        try:
            tree = ast.parse(code)
            
            # 计算圈复杂度（简化版）
            complexity = 1  # 基础复杂度
            
            for node in ast.walk(tree):
                if isinstance(node, (ast.If, ast.For, ast.While, ast.ExceptHandler)):
                    complexity += 1
                elif isinstance(node, ast.And) or isinstance(node, ast.Or):
                    complexity += 1
            
            return {
                "cyclomatic_complexity": complexity,
                "complexity_level": self._get_complexity_level(complexity)
            }
        except:
            return {
                "cyclomatic_complexity": 0,
                "complexity_level": "unknown"
            }
    
    def _get_complexity_level(self, complexity: int) -> str:
        """获取复杂度等级"""
        if complexity <= 5:
            return "low"
        elif complexity <= 10:
            return "medium"
        elif complexity <= 20:
            return "high"
        else:
            return "very_high"
