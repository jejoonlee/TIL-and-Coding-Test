
import java.util.*;
class TrieNode {
    HashMap<Character, TrieNode> child;
    Boolean isLast;

    TrieNode () {
        this.child = new HashMap<>();
        this.isLast = false;
    }
}

class TrieTree{
    TrieNode root;

    TrieTree() {
        this.root = new TrieNode();
    }

    public void insert(String string) {
        TrieNode current = this.root;

        for (int i = 0; i < string.length(); i ++) {
            char alphabet = string.charAt(i);

            // 다음 child에서 alphabet과 동일한 key가 있으면 넘어가고,
            // 없으면 추가해주는 것이다
            current.child.putIfAbsent(alphabet, new TrieNode());

            // 다음 자식 노드로 옮긴다
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

            if (current.child.containsKey(alphabet)) {
                current = current.child.get(alphabet);
            } else {
                return false;
            }

            if (i == string.length() - 1) {
                if (!current.isLast) {
                    return false;
                }
            }
        }
        return true;
    }

    public void delete(String string) {
        boolean result = delete(this.root, string, 0);

        if (!result) {
            System.out.println(string + " 단어가 없음");
        } else {
            System.out.println(string + " 단어가 삭제 됨");
        }
    }

    public boolean delete(TrieNode node, String string, int idx) {
        char alphabet = string.charAt(idx);


        if (!node.child.containsKey(alphabet)) {
            return false;
        }

        TrieNode current = node.child.get(alphabet);
        idx ++;

        // 마지막 알파벳에 도달
        if (idx == string.length()) {

            // 마지막 알파벳이 트리에서 마지막으로 표시가 안 되어 있으면 false를 반환
            if (!current.isLast) {
                return false;
            }

            // 그것이 아니면, 나중에 삭제를 하기 위해, true에서 false로 만든다
            current.isLast = false;

            // 자식 노드에 아무것도 없으면 해당 현재 node의 자식 노드를 삭제한다
            // 다음 자식 노드에 알파벳이 있으면, 그냥 단어의 마지막인 유무를 바꾸기만 하면 된다
            if (current.child.isEmpty()) {
                node.child.remove(alphabet);
            }
        } else {
            // 1을 더한 인덱스를 통해 재귀 함수를 실행한다
            if (!delete(node, string, idx)) return false;

            // 현재 노드가 마지막이 아닐 경우, 그리고 자식 노드가 비어 있을 경우
            // 노드의 자식 노드 (즉 현재 노드) 를 삭제한다
            if (!current.isLast && current.child.isEmpty()) {
                node.child.remove(alphabet);
            }
        }
        return true;
    }
}

public class trie {

    public static void main(String[] args) {

        TrieTree trieTree = new TrieTree();
        trieTree.insert("action");
        trieTree.insert("act");
        trieTree.insert("actor");
        trieTree.insert("best");
        trieTree.insert("beast");
        trieTree.insert("bored");


        trieTree.delete("act");

        System.out.println(trieTree.search("action"));
        System.out.println(trieTree.search("act"));
        System.out.println(trieTree.search("actor"));
        System.out.println(trieTree.search("acting"));
        System.out.println(trieTree.search("best"));
        System.out.println(trieTree.search("beast"));
        System.out.println(trieTree.search("bored"));



    }
}
