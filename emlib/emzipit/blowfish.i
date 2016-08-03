%module blowfish
%{
#include "blowfish.h"
extern void BF_set_key(BF_KEY *key, int len, const unsigned char *data);

extern void BF_encrypt(BF_LONG *data, const BF_KEY *key);
extern void BF_decrypt(BF_LONG *data, const BF_KEY *key);

extern void BF_ecb_encrypt(const unsigned char *in, unsigned char *out,
                    const BF_KEY *key, int enc);
extern void BF_cbc_encrypt(const unsigned char *in, unsigned char *out, long length,
                    const BF_KEY *schedule, unsigned char *ivec, int enc);
extern void BF_cfb64_encrypt(const unsigned char *in, unsigned char *out,
                      long length, const BF_KEY *schedule,
                      unsigned char *ivec, int *num, int enc);
extern void BF_ofb64_encrypt(const unsigned char *in, unsigned char *out,
                      long length, const BF_KEY *schedule,
                      unsigned char *ivec, int *num);
%}

extern void BF_set_key(BF_KEY *key, int len, const unsigned char *data);

extern void BF_encrypt(BF_LONG *data, const BF_KEY *key);
extern void BF_decrypt(BF_LONG *data, const BF_KEY *key);

extern void BF_ecb_encrypt(const unsigned char *in, unsigned char *out,
                    const BF_KEY *key, int enc);
extern void BF_cbc_encrypt(const unsigned char *in, unsigned char *out, long length,
                    const BF_KEY *schedule, unsigned char *ivec, int enc);
extern void BF_cfb64_encrypt(const unsigned char *in, unsigned char *out,
                      long length, const BF_KEY *schedule,
                      unsigned char *ivec, int *num, int enc);
extern void BF_ofb64_encrypt(const unsigned char *in, unsigned char *out,
                      long length, const BF_KEY *schedule,
                      unsigned char *ivec, int *num);
