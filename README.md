# Wind Load Calculator

This repository provides a simple Python script `wind_load.py` to estimate facade
wind loads using the methodology of Australian Standard **AS/NZS 1170.2**.
The implementation is simplified for educational use and should not be relied
upon for final engineering design without verification.

## Usage

Run the script with the required parameters:

```bash
python wind_load.py Vr Md Ms Mt Mz_cat Cp [--density D] [--area A]
```

Parameters:
- `Vr` regional basic wind speed in m/s.
- `Md` wind direction multiplier.
- `Ms` shielding multiplier.
- `Mt` topographic multiplier.
- `Mz_cat` terrain/height multiplier.
- `Cp` external pressure coefficient.
- `--density` optional air density in kg/m³ (default 1.2).
- `--area` optional area in m² to compute total wind load.

Example:

```bash
python wind_load.py 45 1.0 1.0 1.0 0.95 0.8 --area 10
```
