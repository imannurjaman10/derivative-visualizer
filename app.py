import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# ===========================
# APP CONFIG
# ===========================
st.set_page_config(page_title="Math WebApp – PR1 & PR2", layout="centered")

# ===========================
# SIDEBAR NAVIGATION
# ===========================
menu = st.sidebar.radio(
    "Navigation",
    ["Function & Derivative Visualizer", "Optimization Solver"]
)

# ===========================
# PAGE 1 — FUNCTION & DERIVATIVE (PR1)
# ===========================
if menu == "Function & Derivative Visualizer":
    st.title("Function & Derivative Visualizer (PR1)")

    st.write("Masukkan fungsi f(x) untuk melihat grafik dan turunannya.")

    user_func_str = st.text_input("Fungsi f(x) :", "x**2")

    col1, col2 = st.columns(2)
    with col1:
        x_min = st.number_input("x minimum", value=-10.0)
    with col2:
        x_max = st.number_input("x maksimum", value=10.0)

    num_points = st.slider("Jumlah titik (resolution)", 100, 2000, 400)

    x = sp.symbols('x')

    if st.button("Hitung & Tampilkan Grafik"):
        try:
            f_expr = sp.sympify(user_func_str)
            f_prime_expr = sp.diff(f_expr, x)

            st.subheader("Turunan Fungsi")
            st.latex(r"f(x) = " + sp.latex(f_expr))
            st.latex(r"f'(x) = " + sp.latex(f_prime_expr))

            f_num = sp.lambdify(x, f_expr, "numpy")
            f_prime_num = sp.lambdify(x, f_prime_expr, "numpy")

            xs = np.linspace(x_min, x_max, num_points)
            ys = f_num(xs)
            ys_p = f_prime_num(xs)

            st.subheader("Grafik f(x)")
            fig1, ax1 = plt.subplots()
            ax1.plot(xs, ys)
            ax1.grid()
            st.pyplot(fig1)

            st.subheader("Grafik f'(x)")
            fig2, ax2 = plt.subplots()
            ax2.plot(xs, ys_p, color="orange")
            ax2.grid()
            st.pyplot(fig2)

        except Exception as e:
            st.error(f"Error: {e}")

# ===========================
# PAGE 2 — OPTIMIZATION SOLVER (PR2)
# ===========================
if menu == "Optimization Solver":
    st.title("Optimization Solver (PR2)")
    st.write("Selesaikan masalah optimasi (area, perimeter, volume, profit).")

    problem = st.selectbox(
        "Pilih jenis masalah optimasi:",
        ["Max Area (keliling tetap)",
         "Max Volume (box tanpa tutup)",
         "Min Perimeter (luas tetap)",
         "Max Profit"]
    )

    x = sp.symbols("x")

    # ========== MAX AREA ==========
    if problem == "Max Area (keliling tetap)":
        st.subheader("Maximize Area with Fixed Perimeter")

        P = st.number_input("Masukkan keliling (P):", value=40.0)

        st.write("Misalkan taman berbentuk persegi panjang:")
        st.latex("P = 2x + 2y")
        st.latex(r"A = x \cdot y")


        # Using substitution: y = (P/2) - x
        y_expr = (P/2) - x
        A_expr = x * y_expr
        dA = sp.diff(A_expr, x)

        st.write("Fungsi luas:")
        st.latex("A(x) = " + sp.latex(A_expr))

        st.write("Turunan:")
        st.latex("A'(x) = " + sp.latex(dA))

        critical = sp.solve(dA, x)[0]
        y_val = y_expr.subs(x, critical)

        st.success(f"Luas maksimum terjadi pada x = {critical}, y = {y_val}")
        st.info(f"**Solusi:** Taman persegi panjang memiliki ukuran optimum ketika x = y (bentuk persegi).")

    # ========== MAX VOLUME ==========
    if problem == "Max Volume (box tanpa tutup)":
        st.subheader("Maximize Volume – Open Box")

        L = st.number_input("Panjang karton:", value=20.0)
        W = st.number_input("Lebar karton:", value=20.0)

        st.write("Volume:")
        st.latex("V = x(L - 2x)(W - 2x)")

        V_expr = x * (L - 2*x) * (W - 2*x)
        dV = sp.diff(V_expr, x)
        critical = sp.solve(dV, x)[0]

        st.success(f"x optimum = {critical}")
        st.info(f"Volume maksimum dicapai saat tinggi lipatan = {critical}")

    # ========== MIN PERIMETER ==========
    if problem == "Min Perimeter (luas tetap)":
        st.subheader("Minimize Perimeter with Fixed Area")

        A = st.number_input("Masukkan luas (A):", value=50.0)

        y_expr = A/x
        P_expr = 2*(x + y_expr)
        dP = sp.diff(P_expr, x)
        critical = sp.solve(dP, x)[0]
        y_val = y_expr.subs(x, critical)

        st.success(f"Keliling minimum terjadi pada x = {critical}, y = {y_val}")
        st.info("Bentuk terbaik adalah persegi.")

    # ========== MAX PROFIT ==========
    if problem == "Max Profit":
        st.subheader("Maximize Profit")

        st.write("Masukkan fungsi Revenue (R) dan Cost (C) dalam variabel x")

        R_str = st.text_input("Revenue R(x):", "50*x - x**2")
        C_str = st.text_input("Cost C(x):", "10*x + 5")

        R_expr = sp.sympify(R_str)
        C_expr = sp.sympify(C_str)

        P_expr = R_expr - C_expr
        dP = sp.diff(P_expr, x)
        critical = sp.solve(dP, x)[0]

        st.latex("Profit = R(x) - C(x)")
        st.latex("P(x) = " + sp.latex(P_expr))

        st.success(f"Profit maksimum ketika x = {critical}")
