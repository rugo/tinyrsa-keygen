from Crypto.PublicKey import RSA
from Crypto.Util import number
import secrets
import sys

FILE_NAME_TEMPLATE = "output/{bit_length}bit_{name}_{type}.pem"

def gen(bit_len):
    bit_len_half = bit_len // 2
    bit_len_remainder = bit_len % 2
    found = False

    while not found:
        try:
            p = number.getPrime(bit_len_half)
            q = number.getPrime(bit_len_half + bit_len_remainder)

            phi = (p-1)*(q-1)
            N = p * q
            
            # e would usually be a small prime number with low 
            # hamming weight, typically 65537
            # As we only care about integer factorization, 
            # that doesnt matter for us
            e = 3
            d = pow(e, -1, phi)
            privkey = RSA.construct((N, e, d))
            found = True
        except ValueError:
            continue

    return privkey, privkey.public_key()

def write_key_file(key, bit_len, name):
    with open(
        FILE_NAME_TEMPLATE.format(
            bit_length=bit_len,
            name=name,
            type="private" if key.has_private() else "public"),
            "wb"
        ) as f:
        f.write(key.export_key("PEM"))

def main():
    if len(sys.argv) < 2:
        print(f"Call with: {sys.argv[0]} $BIT_LEN")
        sys.exit(1)
    
    bit_len = int(sys.argv[1])
    key_name = secrets.token_hex(16)
    
    privkey, pubkey = gen(bit_len)

    write_key_file(privkey, bit_len, key_name)
    write_key_file(pubkey, bit_len, key_name)
    
    print(f"> Wrote keys with identifier '{key_name}'")

if __name__ == '__main__':
    main()