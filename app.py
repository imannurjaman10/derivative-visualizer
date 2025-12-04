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

    # ==========================================
#  STORY-BASED OPTIMIZATION PROBLEM SOLVER
# ==========================================
st.sidebar.markdown("### 📝 Story Problem Solver")

st.header("🧩 Story-Based Optimization Solver (PR2 Upgrade)")

st.write("""
Masukkan soal cerita yang berkaitan dengan **luas, keliling, volume, atau profit**.
Sistem akan mencoba membaca konteks, menyusun model matematis, dan mencari nilai optimum.
""")

# Contoh soal otomatis agar mahasiswa tidak bingung
example = st.selectbox("Pilih contoh soal (opsional):", [
    "—",
    "Taman persegi panjang dengan keliling 40 m, luas maksimum",
    "Kotak tanpa tutup dengan volume maksimum dari karton 600 cm²",
    "Fungsi profit P = ax - bx², cari x optimal",
    "Permintaan linear: harga p = 100 - 2x, cari revenue maksimum"
])

def load_example(text):
    if text == "Taman persegi panjang dengan keliling 40 m, luas maksimum":
        return "Sebuah taman berbentuk persegi panjang memiliki keliling 40 meter. Tentukan ukuran taman agar luasnya maksimum."
    if text == "Kotak tanpa tutup dengan volume maksimum dari karton 600 cm²":
        return "Sebuah kotak tanpa tutup akan dibuat dari karton berukuran 600 cm². Tentukan ukuran alas dan tinggi agar volumenya maksimum."
    if text == "Fungsi profit P = ax - bx², cari x optimal":
        return "Sebuah perusahaan memiliki fungsi profit P(x) = 50x - 2x². Tentukan jumlah produksi yang memaksimalkan profit."
    if text == "Permintaan linear: harga p = 100 - 2x, cari revenue maksimum":
        return "Harga barang mengikuti fungsi permintaan p = 100 - 2x. Tentukan jumlah penjualan yang memaksimalkan revenue."
    return ""

story_input = st.text_area("Masukkan soal cerita:", value=load_example(example), height=140)

solve = st.button("🔍 Solve Problem")

import sympy as sp
import re

def extract_numbers(text):
    """Ambil semua angka dalam teks"""
    nums = re.findall(r"\d+\.?\d*", text)
    return [float(n) for n in nums]

def detect_type(text):
    text = text.lower()
    if "luas" in text or "area" in text:
        return "area"
    if "keliling" in text or "perimeter" in text:
        return "perimeter"
    if "volume" in text:
        return "volume"
    if "profit" in text or "keuntungan" in text:
        return "profit"
    if "revenue" in text or "permintaan" in text:
        return "revenue"
    return "unknown"


# =============================================================
# Main solver logic
# =============================================================

if solve:
    if len(story_input.strip()) < 10:
        st.error("Masukkan soal dengan jelas.")
    else:
        st.subheader("📘 Analisis Soal")
        numbers = extract_numbers(story_input)
        tipe = detect_type(story_input)

        st.write(f"**Tipe soal terdeteksi:** `{tipe}`")
        st.write(f"**Angka ditemukan:** `{numbers}`")

        x = sp.symbols("x")

        # ===================================
        # CASE 1: Luas maksimum dengan keliling
        # ===================================
        if tipe == "area" and "keliling" in story_input.lower():
            P = numbers[0]

            st.write("### Model Matematis")
            st.latex(r"P = 2x + 2y")
            st.latex(r"y = \frac{P}{2} - x")

            A = x * ((P/2) - x)
            dA = sp.diff(A, x)
            xc = sp.solve(dA)[0]

            yc = (P/2) - xc
            Amax = A.subs(x, xc)

            st.success("### Hasil")
            st.write(f"x optimum = **{float(xc):.2f}**")
            st.write(f"y optimum = **{float(yc):.2f}**")
            st.write(f"Luas maksimum = **{float(Amax):.2f} m²**")

        # ===================================
        # CASE 2: Volume kotak tanpa tutup
        # ===================================
        elif tipe == "volume" and ("tanpa tutup" in story_input.lower()):
            A = numbers[0]  # total luas karton

            st.write("### Model Matematis")
            st.latex(r"A = x^2 + 4xh")

            h = sp.symbols("h")
            eq = sp.Eq(x**2 + 4*x*h, A)
            h_expr = sp.solve(eq, h)[0]

            Volume = x**2 * h_expr
            dV = sp.diff(Volume, x)
            xc = sp.solve(dV)[0]
            h_opt = h_expr.subs(x, xc)
            Vmax = Volume.subs(x, xc)

            st.success("### Hasil Volume Maksimum")
            st.write(f"Ukuran alas x = **{float(xc):.2f}** cm")
            st.write(f"Tinggi h = **{float(h_opt):.2f}** cm")
            st.write(f"Volume maksimum = **{float(Vmax):.2f} cm³**")

        # ===================================
        # CASE 3: Profit P = ax - bx²
        # ===================================
        elif tipe == "profit":
            a, b = numbers[0], numbers[1]
            P = a*x - b*x**2

            dP = sp.diff(P, x)
            xc = sp.solve(dP)[0]
            maxP = P.subs(x, xc)

            st.success("### Profit Maksimum")
            st.write(f"Jumlah produksi optimum = **{float(xc):.2f} unit**")
            st.write(f"Profit maksimum = **{float(maxP):,.2f}**")

        # ===================================
        # CASE 4: Revenue R = x * p(x)
        # ===================================
        elif tipe == "revenue":
            # asumsi bentuk p = a - bx
            a, b = numbers[0], numbers[1]
            p = a - b*x
            R = x * p

            dR = sp.diff(R, x)
            xc = sp.solve(dR)[0]
            Rmax = R.subs(x, xc)

            st.success("### Revenue Maksimum")
            st.write(f"Jumlah penjualan optimum = **{float(xc):.2f} unit**")
            st.write(f"Revenue maksimum = **{float(Rmax):,.2f}**")

        # ===================================
        # Default: tidak dikenali
        # ===================================
        else:
            st.warning("Soal belum didukung otomatis. Gunakan bentuk yang lebih standar.")

