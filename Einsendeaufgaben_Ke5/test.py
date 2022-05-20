
def euler(t, n, x0, y0):
    xn = [x0]
    yn = [y0]
    delta_t = t / n
    for i in range(n - 1):
        derivative_dx = 1.1 * xn[-1] - 0.4 * xn[-1] * yn[-1]
        xn_i1 = xn[-1] + derivative_dx * delta_t

        derivative_dy = 0.1 * xn[-1] * yn[-1] - 0.4 * yn[-1]
        yn_i1 = yn[-1] + derivative_dy * delta_t

        xn.append(xn_i1)
        yn.append(yn_i1)
    return xn, yn