# RSA Key Generator
This script generates RSA keys of arbitrary modulus size and saves them in `PEM` format.
**The output should only be used for research as small keys break the security of RSA.**

To use the script you need **Python >= 3.8** and **PyCryptoDome**.

Install PyCryptoDome with:

```bash
pip install -r requirements.txt
```

Generate a 20 bit key with:

```bash
python main.py 20
```

Generate keys of sizes 10 to 256 bit:

```bash
for i in {10..256}; do
    python main.py $i
done
```

Keys are writte to the `output` directory. Works reliable for keys with size > 10bit.
