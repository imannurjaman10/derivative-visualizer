import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Function & Derivative Visualizer")

st.title("Function & Derivative Visualizer")
st.write(
    "Webapp sederhana untuk menampilkan grafik suatu fungsi, menghitung turunan pertama, "
    "dan menampilkan grafik fungsi turunannya."
)

st.subheader("1. Masukkan Fungsi")
st.write("Gunakan variabel **x**. Contoh: `x**2`, `sin(x)`, `exp(x)`, `x**3 - 4*x + 1`.")

user_func_str = st.text_input("Fungsi f(x) =", "x**2")

col1, col2 = st.columns(2)
with col1:
    x_min = st.number_input("Batas x minimum", value=-10.0)
with col2:
    x_max = st.number_input("Batas x maksimum", value=10.0)

num_points = st.slider("Jumlah titik untuk plotting", min_value=50, max_value=1000, value=400, step=50)

x = sp.symbols("x")

if st.button("Hitung & Tampilkan Grafik"):
    try:
        # Ubah input string menjadi ekspresi sympy
        f_expr = sp.sympify(user_func_str)

        # Hitung turunan pertama
        f_prime_expr = sp.diff(f_expr, x)

        st.subheader("2. Hasil Turunan")
        st.write("Turunan pertama dari fungsi:")
        st.latex(r"f(x) = " + sp.latex(f_expr))
        st.latex(r"f'(x) = " + sp.latex(f_prime_expr))

        # Konversi ke fungsi numerik untuk plotting
        f_num = sp.lambdify(x, f_expr, "numpy")
        f_prime_num = sp.lambdify(x, f_prime_expr, "numpy")

        # Buat range x
        xs = np.linspace(x_min, x_max, num_points)

        # Hitung nilai fungsi dan turunannya
        ys = f_num(xs)
        ys_prime = f_prime_num(xs)

        # Plot f(x)
        st.subheader("3. Grafik Fungsi f(x)")
        fig1, ax1 = plt.subplots()
        ax1.plot(xs, ys, label="f(x)")
        ax1.set_xlabel("x")
        ax1.set_ylabel("f(x)")
        ax1.grid(True)
        ax1.legend()
        st.pyplot(fig1)

        # Plot f'(x)
        st.subheader("4. Grafik Turunan f'(x)")
        fig2, ax2 = plt.subplots()
        ax2.plot(xs, ys_prime, label="f'(x)")
        ax2.set_xlabel("x")
        ax2.set_ylabel("f'(x)")
        ax2.grid(True)
        ax2.legend()
        st.pyplot(fig2)

    except Exception as e:
        st.error(f"Terjadi error: {e}")

st.markdown("---")
st.caption(
    "Dibuat untuk tugas webapp: menampilkan grafik fungsi, menghitung turunan, dan menampilkan grafik fungsi turunan."
)
