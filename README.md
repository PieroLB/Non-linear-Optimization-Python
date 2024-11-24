The LP Problem :
```math
\begin{align*}
\text{max} \quad & x_1 + 4x_2 + 2x_3 \\
\text{s.t} \quad & 5x_1 + 2x_2 + 2x_3 \leq 145 \\
& 4x_1 + 8x_2 - 8x_3 \leq 260 \\
& x_1 + x_2 + 4x_3 \leq 190 \\
& x_1, x_2, x_3 ≥ 0
\end{align*}
```

# 1. Write the dual LP problem
Dual LP Problem :
```math
\begin{align*}
\text{min} \quad & 145y_1 + 260y_2 + 190y_3 \\
\text{s.t} \quad & 5y_1 + 4y_2 + y_3 \geq 1 \\
& 2y_1 + 8y_2 + y_3 \geq 4 \\
& 2y_1 - 8y_2 + 4y_3 \geq 2 \\
& y_1, y_2, y_3 ≥ 0
\end{align*}
```
Code :
```
print(convert_to_dual(
  [ ["x1",0,"inf"], ["x2",0,"inf"], ["x3",0,"inf"] ],
  [ [[5,2, 2],"<=",145.0], [[4,8,-8],"<=",260.0], [[1,1,4],"<=",190.0] ],
  [1,4,2]
))
```
Output :
```
([('y1', 0, 'inf'), ('y2', 0, 'inf'), ('y3', 0, 'inf')], [([5, 4, 1], '>=', 1), ([2, 8, 1], '>=', 4), ([2, -8, 4], '>=', 2)], [145.0, 260.0, 190.0])
```
# 2. Verify that $Q=(x_1,x_2,x_3)=(0,52.5,20)$ is a feasible solution for the primal
We check if this solution satisfies the primal constraints:
```math
\begin{align*}
& 5x_1​+2x_2​+2x_3​=5*0+2*52.5+2*20=105+40=145 \leq 145 \\
& 4x_1​+8x_2​−8x_3​=4*0+8*52.5−8*20=420−160=260 \leq 260 \\
& x_1​+x_2​+4x_3​=0+52.5+4*20=52.5+80=132.5 \leq 190 \\
& x_1​ = 0 \geq 0 \\
& x_2​ = 52.5 \geq 0 \\
& x_3 = 20 \geq 0
\end{align*}
```
Code :
```
print(is_a_feasable_region(
    [ 0 , 52.5 , 20 ],
    [ [[5,2,2],"<=",145.0], [[4,8,-8],"<=",260.0], [[1,1,4],"<=",190.0] ]
))
```
Output :
```
True
```
All the primal constraints are satisfying by this solution. Therefore, $Q=(x_1,x_2,x_3)=(0,52.5,20)$ is a feasible solution for the primal.
# 3. Use CS to determine a candidate solution to the dual
```math
\begin{align*}
& X = (0,52.5,20)\\
& 145 - (5*0 + 2*52.5 + 2*20) = 0 \\
& 260 - (4*0 + 8*52.5 - 8*20) = 0 \\
& 190 - (0 + 52.5 + 4*20) = 57,5 \\
& \begin{pmatrix}
0\\
0\\
57,5
\end{pmatrix}.Y = 0 => Y_3=0\\
& \begin{cases}
2y_1+8y_2=4\\
2y_1-8y_2=2
\end{cases}
=>
\begin{cases}
y_1=3/2\\
y_2=1/8\\
y_3=0
\end{cases}
\end{align*}
```
# 4. Is $Q$ the solution for the primal problem?
```math
\begin{align*}
& b.Y =
\begin{pmatrix}
3/2\\
1/8\\
0
\end{pmatrix}.
\begin{pmatrix}
145\\
260\\
190
\end{pmatrix}=3/2*145+1/8*260+0*190=250
\end{align*}
```
