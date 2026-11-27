from pyscript import document # type: ignore #type: ignore from Google
from pyscript.ffi import create_proxy # type: ignore #type: ignore from Google

non_metals = {
    "H": ("Hydrogen", 1, 1.008),
    "He": ("Helium", 2, 4.0026),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "Ne": ("Neon", 10, 20.180),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "Cl": ("Chlorine", 17, 35.45),
    "Ar": ("Argon", 18, 39.948),
    "Se": ("Selenium", 34, 78.971),
    "Br": ("Bromine", 35, 79.904),
    "Kr": ("Krypton", 36, 83.798),
    "I": ("Iodine", 53, 126.904),
    "Xe": ("Xenon", 54, 131.293),
    "Rn": ("Radon", 86, 222),
}

def format_symbol(text):
    cleaned = text.strip()
    if not cleaned:
        return ""
    return cleaned[0].upper() + cleaned[1:].lower()

def search_element(e=None):
    result_section = document.getElementById("result_section")
    result_box = document.getElementById("result")
    result_section.style.display = "block"

    raw_input = document.getElementById("element_input").value
    symbol = format_symbol(raw_input)

    name, atomic_num, atomic_mass = non_metals.get(
        symbol,
        ("Element does not exist in the non-metals list.", "-", "-")
    )

    display_symbol = symbol if symbol else "None entered"

    result_box.innerHTML = f"""
        <div>Symbol: <span style="color: #7b8ec2;">{display_symbol}</span></div>
        <div>Element: <span style="color: #7b8ec2;">{name}</span></div>
        <div>Atomic Number: <span style="color: #7b8ec2;">{atomic_num}</span></div>
        <div>Atomic Mass: <span style="color: #7b8ec2;">{atomic_mass}</span></div>
    """

def on_enter(event):
    if event.key == "Enter":
        search_element(event)

click_proxy = create_proxy(search_element)
enter_proxy = create_proxy(on_enter)

document.getElementById("check_btn").addEventListener("click", click_proxy)
document.getElementById("element_input").addEventListener("keypress", enter_proxy)

status_el = document.getElementById("py_status")
if status_el:
    status_el.style.display = "none"
