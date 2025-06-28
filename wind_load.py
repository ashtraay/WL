"""Calculate facade wind loads based on Australian Standard AS/NZS 1170.2.

This script implements a simplified approach for educational purposes.
It computes design wind pressure on a building facade given the basic
wind speed and multipliers defined in the standard.

Formulas:
    Vdes = Vr * Md * Ms * Mt * Mz_cat
    qz = 0.5 * density * Vdes**2
    P = qz * Cp

Where:
    Vr      - regional basic wind speed (m/s)
    Md      - wind direction multiplier
    Ms      - shielding multiplier
    Mt      - topographic multiplier
    Mz_cat  - terrain/height multiplier
    Cp      - external pressure coefficient
    density - air density (default 1.2 kg/m^3)

If an area is supplied, the resulting wind load in Newtons is returned
as P * area.
"""
import argparse

DEFAULT_DENSITY = 1.2  # kg/m^3


def design_wind_speed(vr, md, ms, mt, mz_cat):
    """Calculate design wind speed Vdes."""
    return vr * md * ms * mt * mz_cat


def design_pressure(vdes, cp, density=DEFAULT_DENSITY):
    """Calculate design wind pressure on a facade."""
    qz = 0.5 * density * vdes ** 2
    return qz * cp


def parse_args():
    parser = argparse.ArgumentParser(description="Facade wind load calculator")
    parser.add_argument("vr", type=float, help="Regional basic wind speed Vr (m/s)")
    parser.add_argument("md", type=float, help="Wind direction multiplier Md")
    parser.add_argument("ms", type=float, help="Shielding multiplier Ms")
    parser.add_argument("mt", type=float, help="Topographic multiplier Mt")
    parser.add_argument("mz_cat", type=float, help="Terrain/height multiplier Mz_cat")
    parser.add_argument("cp", type=float, help="External pressure coefficient Cp")
    parser.add_argument("--density", type=float, default=DEFAULT_DENSITY,
                        help="Air density in kg/m^3 (default 1.2)")
    parser.add_argument("--area", type=float, default=None,
                        help="Area in square meters to calculate total load")
    return parser.parse_args()


def main():
    args = parse_args()
    vdes = design_wind_speed(args.vr, args.md, args.ms, args.mt, args.mz_cat)
    pressure = design_pressure(vdes, args.cp, args.density)
    print(f"Design wind speed Vdes: {vdes:.2f} m/s")
    print(f"Design pressure: {pressure:.2f} Pa")
    if args.area is not None:
        load = pressure * args.area
        print(f"Resulting load on {args.area} m^2: {load:.2f} N")


if __name__ == "__main__":
    main()
