# Tools

Graphing and visualisation:

- [Gitlab flavoured markdown](https://docs.gitlab.com/ee/user/markdown.html) is extremely flexible, supporting mermaid syntax, a subset of latex math

- Writing [latex equations online](https://www.hostmath.com/)

- Vscode plugin for renderding markdown with digrams and latex math [Markdown Preview Enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced)

# Sum of finite arithmetic series

```math
S_n = \sum_{n=1}^{n} a+ (n-1)d \\
```
Expand and re-arrange
```math
S_n = a + (a + d) + (a + 2d) + ... +  (a + (n-2)d) + (a + (n-1)d) \\
S_n = (a + (n-1)d) + (a + (n-2)d) + ... + (a + 2d) + (a + d) + a \\
```
Add both to each other
```math
2S_n = n(2a + (n-1)d) \\
S_n = \frac{n}{2}(2a + (n-1)d) \\
```

# Sum of Geometric series

```math
S_n = \sum_{n=0}^{n} ar^{n} = a(\frac{1-r^{n+1}}{1-r})
```

```math
S_n  = a + ar + ar^{2} + ar^{3} + .. + ar^{n-1} + ar^{n} \\
rS_n = ar + ar^{2} + ar^{3} + ... + ar^{n} + ar^{n+1} \\
S_n - rS_n = a - ar^{n+1} \\
(1-r)S_n = a(1-r^{n+1}) \\
S_n = a(\frac{1-r^{n+1}}{1-r})
```
# Stirlings approximation

```math
\ln n! = n \ln n - n + O(\ln n)
```