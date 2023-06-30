import java.util.Arrays;

public class Practice2 {
    public static void solution(String[] dictionary, String sentence) {

        Trie trie = new Trie();

        for (String word : dictionary) trie.insert(word);

        String[] words = sentence.split(" ");
        StringBuilder sb = new StringBuilder();
        StringBuilder answer = new StringBuilder();

        System.out.println(Arrays.toString(words));

        for (int i = 0; i < words.length; i++) {
            TrieNode current = trie.root;

            for (int j = 0; j < words[i].length(); j++) {
                char alphabet = words[i].charAt(j);

                if (current.child.containsKey(alphabet)) {
                    sb.append(alphabet);
                    current = current.child.get(alphabet);

                    if (current.isLast) {
                        answer.append(sb + " ");
                        sb = new StringBuilder();
                        break;
                    }
                } else {
                    answer.append(words[i] + " ");
                    sb = new StringBuilder();
                    break;
                }
            }
        }
        System.out.println(answer);
    }

    public static void main(String[] args) {
        String[] dictionary = {"cat", "bat", "rat"};
        String sentence = "the cattle was rattled by the battery";
        solution(dictionary, sentence);

        dictionary = new String[] {"a", "b", "c"};
        sentence = "apple banna carrot water";
        solution(dictionary, sentence);
    }
}
