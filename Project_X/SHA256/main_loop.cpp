#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <bitset>
using namespace std;

unsigned rotr(unsigned n, int k)
{
    unsigned i,bit;
    for (i=0; i<k; i++)
    {
        bit = n & 0x00000001;
        n >>= 1;
        n |= bit << 31;
    }
    return n;
}

int main(int argc, char *argv[])
{
	stringstream convert(argv[1]);
	unsigned rows;
	convert >> rows;
    //string path = argv[1];

	unsigned cols = 64;
    unsigned **w = new unsigned*[rows];
    for (int i = 0; i < rows; i++)
        w[i] = new unsigned[cols];

    /*ifstream fin;
	fin.open(path);
    if (!fin.is_open())
    {
        return 0;
    }
    else
    {
        for (int i=0; i<rows; i++)
        {
            for (int j=0; j<16; j++)
            {
                fin >> w[i][j];
            }
        }
    }
    fin.close();*/
    for (int i=0; i<rows; i++)
        {
            for (int j=0; j<16; j++)
            {
                w[i][j] = strtoul(argv[2 + i*16 + j], NULL, 10);
            }
        }

    unsigned H[8] = {0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
                     0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19};

    unsigned k[64] = {0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
                      0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
                      0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
                      0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
                      0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
                      0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
                      0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
                      0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
                      0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
                      0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
                      0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
                      0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
                      0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
                      0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
                      0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
                      0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2};

    for (int j=0; j<rows; j++)
    {
        for (int i=16; i<64; i++)
        {
            unsigned s0 = rotr(w[j][i-15], 7) ^ rotr(w[j][i-15], 18) ^ (w[j][i-15] >> 3);
            unsigned s1 = rotr(w[j][i-2], 17) ^ rotr(w[j][i-2], 19) ^ (w[j][i-2] >> 10);
            w[j][i] = w[j][i-16] + s0 + w[j][i-7] + s1;
        }

        unsigned a = H[0];
        unsigned b = H[1];
        unsigned c = H[2];
        unsigned d = H[3];
        unsigned e = H[4];
        unsigned f = H[5];
        unsigned g = H[6];
        unsigned h = H[7];

        for (int i=0; i<64; i++)
        {
            unsigned E0 = rotr(a, 2) ^ rotr(a, 13) ^ rotr(a, 22);
            unsigned Ma = (a & b) ^ (a & c) ^ (b & c);
            unsigned t2 = E0 + Ma;
            unsigned E1 = rotr(e, 6) ^ rotr(e, 11) ^ rotr(e, 25);
            unsigned Ch = (e & f) ^ ((~e) & g);
            unsigned t1 = h + E1 + Ch + k[i] + w[j][i];

            h = g;
            g = f;
            f = e;
            e = d + t1;
            d = c;
            c = b;
            b = a;
            a = t1 + t2;
        }
        H[0] += a;
        H[1] += b;
        H[2] += c;
        H[3] += d;
        H[4] += e;
        H[5] += f;
        H[6] += g;
        H[7] += h;
    }

    ofstream fout;
    string path = "C:\\Users\\admin\\Documents\\XXX\\python\\Project_X\\SHA256\\bits\\result.txt";
	fout.open(path);
    if (!fout.is_open())
    {
        return 0;
    }
    else
    {
        for (int i=0; i<8; i++)
            fout << hex << H[i] <<' ';
    }
    return 1;
}