import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# -------------------------------------------------------------------
# PR1 : FUNCTION & DERIVATIVE VISUALIZER
# -------------------------------------------------------------------

def pr1_page():
    st.title("Function & Derivative Visualizer (PR1)")
    st.write("Masukkan fungsi f(x) untuk menampilkan grafik dan turunan pertama.")

    x = sp.Symbol("x")

    func_input = st.text_input("Fungsi f(x):", "x**2")
    xmin = st.number_input("x minimum:", value=-10.0)
    xmax = st.number_input("x maksimum:", value=10.0)
    res = st.slider("Jumlah titik (resolution):", 100, 1000, 400)

    if st.button("Hitung & Tampilkan Grafik"):
        try:
            f = sp.sympify(func_input)
            dfdx = sp.diff(f, x)

            st.latex(f"f(x) = {sp.latex(f)}")
            st.latex(f"f'(x) = {sp.latex(dfdx)}")

            xs = np.linspace(xmin, xmax, res)
            f_lam = sp.lambdify(x, f, "numpy")
            df_lam = sp.lambdify(x, dfdx, "numpy")

            fig, ax = plt.subplots()
            ax.plot(xs, f_lam(xs), label="f(x)")
            ax.plot(xs, df_lam(xs), label="f'(x)")
            ax.legend()
            st.pyplot(fig)

        except Exception as e:
            st.error(f"Error: {e}")

# -------------------------------------------------------------------
# PR2 : OPTIMIZATION STORY PROBLEMS SOLVER
# -------------------------------------------------------------------

def solve_area(perimeter):
    x = sp.symbols('x', positive=True)
    y = (perimeter / 2) - x
    A = x * y
    dA = sp.diff(A, x)
    x_opt = sp.solve(dA, x)[0]
    y_opt = y.subs(x, x_opt)
    A_max = A.subs(x, x_opt)
    return x_opt, y_opt, A_max


def solve_box(L, W, H):
    x = sp.symbols('x', positive=True)
    V = (L - 2*x) * (W - 2*x) * H
    dV = sp.diff(V, x)
    x_opt = sp.solve(dV, x)[0]
    V_max = V.subs(x, x_opt)
    return x_opt, V_max


def solve_profit(R, C):
    x = sp.symbols('x', positive=True)
    P = R - C
    dP = sp.diff(P, x)
    x_opt = sp.solve(dP, x)[0]
    P_max = P.subs(x, x_opt)
    return x_opt, P_max


def pr2_page():
    st.title("Optimization Solver (PR2)")
    st.write("Pilih jenis soal cerita.")

    pilihan = st.selectbox(
        "Jenis Soal:",
        ["Maximize Area (Perimeter)", "Maximize Volume (Box Problem)", "Maximize Profit"]
    )

    # ------------ AREA ------------
    if pilihan == "Maximize Area (Perimeter)":
        P = st.number_input("Masukkan nilai keliling:", value=20.0)
        if st.button("Solve"):
            x_opt, y_opt, A_max = solve_area(P)
            st.success(f"x optimal = {float(x_opt):.2f}, y optimal = {float(y_opt):.2f}")
            st.info(f"Luas maksimum = {float(A_max):.2f}")

    # ------------ BOX VOLUME ------------
    elif pilihan == "Maximize Volume (Box Problem)":
        L = st.number_input("Length:", value=20.0)
        W = st.number_input("Width:", value=10.0)
        H = st.number_input("Height:", value=5.0)
        if st.button("Solve"):
            x_opt, V_max = solve_box(L, W, H)
            st.success(f"Cut size optimal = {float(x_opt):.2f}")
            st.info(f"Volume maksimum = {float(V_max):.2f}")

    # ------------ PROFIT ------------
    elif pilihan == "Maximize Profit":
        st.write("Masukkan fungsi Revenue R(x) dan Cost C(x) menggunakan variabel x.")
        R_inp = st.text_input("Revenue R(x):", "100*x - 0.5*x**2")
        C_inp = st.text_input("Cost C(x):", "20*x + 100")

        x = sp.symbols('x', positive=True)
        R = sp.sympify(R_inp)
        C = sp.sympify(C_inp)

        if st.button("Solve"):
            x_opt, P_max = solve_profit(R, C)
            st.success(f"Produksi optimal = {float(x_opt):.2f}")
            st.info(f"Profit maksimum = {float(P_max):.2f}")

# -------------------------------------------------------------------
# GROUP PROFILE PAGE
# -------------------------------------------------------------------

def group_profile_page():
    st.title("Group Profile")
    st.write("Berikut adalah profil anggota kelompok kami:")

    st.markdown("### 👤 **Member 1**")
    st.write("- **Name:** Iman Nurjaman")
    st.write("- **Student ID:** 004202505003")
    st.write("- **Role:** Developer, Coding, Debugging, Deployment")

    st.markdown("---")

    st.markdown("### 👤 **Member 2**")
    st.write("- **Name:** Nabila Zettiara Rahman")
    st.write("- **Student ID:** 004202505028")
    st.write("- **Role:** Documentation, Testing")

    st.markdown("---")

    st.markdown("### 👤 **Member 3**")
    st.write("- **Name:** Ega Ryan Wardoyo")
    st.write("- **Student ID:** 004202505044")
    st.write("- **Role:** UI/UX Design, Report")

    st.markdown("---")

    st.markdown("### 📌 Group Summary")
    st.write("""
    Our team collaborated to develop a calculus web application using Streamlit. 
    We divided roles for UI design, coding, debugging, optimization features, 
    documentation, and deployment.
    """)

# -------------------------------------------------------------------
# SIDEBAR NAVIGATION
# -------------------------------------------------------------------

st.sidebar.title("Navigation")
menu = st.sidebar.radio("Pilih Halaman:", 
                        ["PR1: Function & Derivative", 
                         "PR2: Optimization Solver",
                         "Group Profile"])

if menu == "PR1: Function & Derivative":
    pr1_page()

elif menu == "PR2: Optimization Solver":
    pr2_page()

elif menu == "Group Profile":
    group_profile_page()
