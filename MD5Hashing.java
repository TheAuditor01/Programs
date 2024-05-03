import java.math.BigInteger;
import java.nio.charset.StandardCharsets;

public class MD5Hashing {

    // Constants for MD5 algorithm
    private static final int[] T = new int[64];
    private static final int[][] S = {
            { 7, 12, 17, 22 },
            { 5, 9, 14, 20 },
            { 4, 11, 16, 23 },
            { 6, 10, 15, 21 }
    };

    static {
        for (int i = 0; i < 64; i++) {
            T[i] = (int) (Math.abs(Math.sin(i + 1)) * Math.pow(2, 32));
        }
    }

    // Helper functions for MD5 algorithm
    private static int leftRotate(int x, int n) {
        return (x << n) | (x >>> (32 - n));
    }

    private static byte[] md5Padding(byte[] message) {
        long originalLength = message.length * 8;
        int paddingLength = (message.length % 64 < 56) ? (56 - message.length % 64) : (120 - message.length % 64);

        byte[] paddedMessage = new byte[message.length + paddingLength + 8];
        System.arraycopy(message, 0, paddedMessage, 0, message.length);
        paddedMessage[message.length] = (byte) 0x80;
        for (int i = 1; i < paddingLength; i++) {
            paddedMessage[message.length + i] = 0;
        }

        // Append original message length in bits
        for (int i = 0; i < 8; i++) {
            paddedMessage[paddedMessage.length - 8 + i] = (byte) ((originalLength >>> (8 * i)) & 0xFF);
        }

        return paddedMessage;
    }

    public static String md5(String input) {
        byte[] message = input.getBytes(StandardCharsets.UTF_8);
        message = md5Padding(message);

        int a = 0x67452301;
        int b = 0xEFCDAB89;
        int c = 0x98BADCFE;
        int d = 0x10325476;

        for (int chunkStart = 0; chunkStart < message.length; chunkStart += 64) {
            int[] words = new int[16];
            for (int i = 0; i < 16; i++) {
                words[i] = (message[chunkStart + 4 * i] & 0xFF) |
                        ((message[chunkStart + 4 * i + 1] & 0xFF) << 8) |
                        ((message[chunkStart + 4 * i + 2] & 0xFF) << 16) |
                        ((message[chunkStart + 4 * i + 3] & 0xFF) << 24);
            }

            int A = a, B = b, C = c, D = d;

            for (int i = 0; i < 64; i++) {
                int F, g;
                if (i < 16) {
                    F = (B & C) | (~B & D);
                    g = i;
                } else if (i < 32) {
                    F = (D & B) | (~D & C);
                    g = (5 * i + 1) % 16;
                } else if (i < 48) {
                    F = B ^ C ^ D;
                    g = (3 * i + 5) % 16;
                } else {
                    F = C ^ (B | ~D);
                    g = (7 * i) % 16;
                }

                int temp = D;
                D = C;
                C = B;
                B = B + leftRotate((A + F + T[i] + words[g]) & 0xFFFFFFFF, S[i / 16][i % 4]);
                A = temp;
            }

            a += A;
            b += B;
            c += C;
            d += D;
        }

        byte[] hashBytes = new byte[16];
        System.arraycopy(BigInteger.valueOf(a).toByteArray(), 0, hashBytes, 0, 4);
        System.arraycopy(BigInteger.valueOf(b).toByteArray(), 0, hashBytes, 4, 4);
        System.arraycopy(BigInteger.valueOf(c).toByteArray(), 0, hashBytes, 8, 4);
        System.arraycopy(BigInteger.valueOf(d).toByteArray(), 0, hashBytes, 12, 4);

        BigInteger hashInt = new BigInteger(1, hashBytes);
        return String.format("%032x", hashInt);
    }

    public static void main(String[] args) {
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        System.out.print("Enter the text to hash using MD5: ");
        String userInput = scanner.nextLine();
        scanner.close();

        String md5Hash = md5(userInput);
        System.out.println("MD5 hash: " + md5Hash);
    }
}
