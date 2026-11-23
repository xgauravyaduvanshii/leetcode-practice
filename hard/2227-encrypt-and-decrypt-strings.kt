// LeetCode 2227. Encrypt and Decrypt Strings — Hard
// https://leetcode.com/problems/encrypt-and-decrypt-strings/
// Submission 2201629151 — Accepted, Kotlin
//
// My thinking: encryption is fixed — every
// letter always becomes the same two — so a
// word's encrypted form is fixed too, and
// decrypting is just counting how many
// dictionary words share that form.

class Encrypter(keys: CharArray, values: Array<String>, dictionary: Array<String>) {
    private val mp = keys.zip(values).toMap()
    private val encCount = mutableMapOf<String, Int>()

    init {
        for (word in dictionary) {
            val enc = encrypt(word)
            if (enc.isNotEmpty()) {
                encCount[enc] = (encCount[enc] ?: 0) + 1
            }
        }
    }

    fun encrypt(word1: String): String {
        val sb = StringBuilder()
        for (c in word1) {
            val v = mp[c] ?: return ""
            sb.append(v)
        }
        return sb.toString()
    }

    fun decrypt(word2: String): Int {
        return encCount[word2] ?: 0
    }
}
