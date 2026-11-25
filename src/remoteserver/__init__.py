import random
from fastmcp import FastMCP

mcp = FastMCP(name="remote server")

@mcp.tool
def add(a: int,b:int) -> int:
    """ Add two numbers,
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of a and b    
    """
    return a+b

@mcp.tool
def multiply(a:int,b:int)->int:
    """ Multply two numbers,    
    
        Args:
            a: First number
            b: Second number
        
        Returns:
            The product of a and b    
    
    """
    return a*b

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
