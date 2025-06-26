from mcp.server.fastmcp import FastMCP
import math

mcp = FastMCP("Hello World")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return int(a + b)

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    return int(a - b)

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return int(a * b)

@mcp.tool()
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    return float(a / b)

@mcp.tool()
def power(a: int, b: int) -> int:
    """Power of two numbers"""
    return int(a**b)

@mcp.tool()
def sqrt(a: int) -> float:
    """Square root of a number"""
    return float(a**0.5)

@mcp.tool()
def cbrt(a: int) -> float:
    """Cube root of a number"""
    return float(a ** (1 / 3))

@mcp.tool()
def factorial(a: int) -> int:
    """factorial of a number"""
    return int(math.factorial(a))

@mcp.tool()
def log(a: int) -> float:
    """log of a number"""
    return float(math.log(a))

@mcp.tool()
def remainder(a: int, b: int) -> int:
    """remainder of two numbers divison"""
    return int(a % b)

@mcp.tool()
def sin(a: int) -> float:
    """sin of a number"""
    return float(math.sin(a))

@mcp.tool()
def cos(a: int) -> float:
    """cos of a number"""
    return float(math.cos(a))

@mcp.tool()
def tan(a: int) -> float:
    """tan of a number"""
    return float(math.tan(a))

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# execute and return the stdio output
if __name__ == "__main__":
    mcp.run(transport="stdio")
