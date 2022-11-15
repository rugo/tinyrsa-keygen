# RSA Key Generator
This script generates RSA keys of arbitrary modulus size and saves them in `PEM` format.
**The output should only be used for research as small keys break the security of RSA.**

TO use the script you need **PyCryptoDome**, install with:

```bash
pip install -r requirements.txt
```

To generate a 20 bit key, do a:

```bash
python main.py 20
```

To generate keys of sizes 10 to 256 bit, do a:

```bash
for i in {10..256}; do
    python main.py $i
done
```

Keys are writte to the `output` directory. Works reliable for keys with size > 10bit.
