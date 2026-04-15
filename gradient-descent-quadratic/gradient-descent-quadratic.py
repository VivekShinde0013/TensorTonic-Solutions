def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here\
    x=x0
    for i in range(1,steps+1):
        gradient=2*a*x+b
        x=x-(lr*gradient)

    return x
    pass