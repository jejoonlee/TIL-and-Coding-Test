import java.util.*;
class TrieNode {
    HashMap<Character, TrieNode> child;
    boolean isLast;

    TrieNode() {
        this.child = new HashMap<Character, TrieNode>();
        this.isLast = false;
    }

}

class Trie {
    TrieNode root;

    Trie() {
        this.root = new TrieNode();
    }

    public void insert(String string) {
        TrieNode current = this.root;

        for (int i = 0; i < string.length(); i++) {
            char alphabet = string.charAt(i);

            if (!current.child.containsKey(alphabet)) {
                current.child.put(alphabet, new TrieNode());
            }

            current = current.child.get(alphabet);

            if (i == string.length() - 1) {
                current.isLast = true;
                return;
            }
        }
    }

    public boolean search(String string) {
        TrieNode current = this.root;

        for (int i = 0; i < string.length(); i++) {
            char alphabet = string.charAt(i);

            if (!current.child.containsKey(alphabet)) {
                return false;
            }

            current = current.child.get(alphabet);

            if (i == string.length() - 1) {
                if (!current.isLast) {
                    return false;
                }
            }
        }
        return true;
    }

    public void delete(String string) {
        boolean getback = delete(this.root, string, 0);
        if (!getback) {
            System.out.println("단어가 없음");
        } else {
            System.out.println(string + " 삭제 완료");
        }
    }
    public boolean delete(TrieNode node, String string, int index){
        char alphabet = string.charAt(index);

        if (!node.child.containsKey(alphabet)) {
            return false;
        }

        TrieNode current = node.child.get(alphabet);
        index ++;

        if (index == string.length()) {
            if (!current.isLast) {
                return false;
            }

            current.isLast = false;

            if (current.child.isEmpty()) {
                node.child.remove(alphabet);
            }
        } else {
            if (!this.delete(current, string, index)) {
                return false;
            }

            if (!current.isLast && current.child.isEmpty()) {
                node.child.remove(alphabet);
            }
        }

        

        return true;
    }

}

public class Main {
    public static void main(String[] args) {
        Trie trie = new Trie();

        trie.insert("action");
        trie.insert("act");
        trie.insert("actor");
        trie.insert("anchor");
        trie.insert("best");
        trie.insert("beast");
        trie.insert("bored");

        trie.delete("actor");
        trie.delete("anchor");

        System.out.println(trie.search("action"));
        System.out.println(trie.search("act"));
        System.out.println(trie.search("actor"));
        System.out.println(trie.search("anchor"));
        System.out.println(trie.search("best"));
        System.out.println(trie.search("beast"));
        System.out.println(trie.search("bored"));
        System.out.println(trie.search("booor"));

    }
}