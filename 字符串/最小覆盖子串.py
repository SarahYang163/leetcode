# https://leetcode.cn/problems/minimum-window-substring/
import collections
import datetime


# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        nt = len(t)
        ns = len(s)
        if nt is ns:
            return t
        for l in range(nt, ns + 1):
            i = 0
            while 0 <= i and i <= ns - l:
                # for i in range(0, ns - l + 1):
                s_tmp = list(s[i:i + l])
                j = 0
                while 0 <= j and j < len(t):
                    if t[j] in s_tmp:
                        s_tmp.remove(t[j])
                    else:
                        break
                    j += 1
                if j == len(t):
                    return s[i:i + l]
                i += 1
        return ""

    # 输入：s = "ADOABC", t = "ABC"
    # 输出："BANC"
    def minWindow1(self, s: str, t: str) -> str:
        count_t = sorted(collections.Counter(t))
        nt = len(t)
        ns = len(s)
        for i in range(nt, ns, 1):
            j = 0
            while j <= ns - nt and j + i <= len(s):
                if t in s[j:j + i]:
                    return s[j:j + i]
                j += 1
        return ""


if __name__ == '__main__':
    # s = "obzcozbufdxgcmesdqnowzpshuwcseenwjqhgsdlxatamysrohfnixfprdsljyyfhrnnjsagtuihuczilgvtfcjwgdhpbixlzmakebszxbhrdibpoxiwztshwczamwnninzmqrmpsviydkptjzpktksrortapgpxwojofxeasoyvyprjoguhqobehugwdvtzlenrcttuitsiijswpogicjolfxhiscjggzzissfcnxnvgftxvbfzkukqrtalvktdjsodmtgzqtuyaqvvrbuexgwqzwduixzrpnvegddyyywaquxjxrnuzlmyipuqotkghfkpknqinoidifnfyczzonxydtqroazxhjnrxfbmtlqcsfhshjrxwqvblovaouxwempdrrplefnxmwrwfjtebrfgrpplcaahpdnzproaxnexnkamzxlwmrniselyeodysirqflpduvibfdvedgcrzpzrunpadvawfsmmddqzaaahfxlifobffbyzqqbtlcpquedzjvykvarayfldvmkapjcfzfbmhscdwhciecsbdledspgpdtsteuafzbrjuvmsfrajtulwirzagiqjdiehefmfifocadxfuxrpsemavncdxuoaetjkavqicgndjkkfhbvbhjdcygfwcwyhpirrfjziqonbyxhibelinpllxsjzoiifscwzlyjturmsaklhnufwcwyhpirrfjziqonbyxhibelinpllxsjzoiifscwzlyjturmsakl"
    # t = "cjgamyzjwxrgwedhsexosmswogckohesskteksqgrjonnrwhywxqkqmywqjlxnfrayykqotkzhxmbwvzstrcjfchvluvbaobymlrcgbbqaprwlsqglsrqvynitklvzmvlamqipryqjpmwhdcsxtkutyfoiqljfhxftnnjgmbpdplnuphuksoestuckgopnlwiyltezuwdmhsgzzajtrpnkkswsglhrjprxlvwftbtdtacvclotdcepuahcootzfkwqhtydwrgqrilwvbpadvpzwybmowluikmsfkvbebrxletigjjlealczoqnnejvowptikumnokysfjyoskvsxztnqhcwsamopfzablnrxokdxktrwqjvqfjimneenqvdxufahsshiemfofwlyiionrybfchuucxtyctixlpfrbngiltgtbwivujcyrwutwnuajcxwtfpatjlzkbuathcuilqzdwfyhwkwxvpicgkxrxweaqevziriwhjzdqanmkljfatjifgaccefukavvsfrbqshhswtchfjkausgaukeapanswimbznstubmswqadckewemzbwdbogogcy"
    s = "ADOABC"
    t = "ABC"

    # res = Solution()
    # print(datetime.datetime.now())

    # print(res.minWindow1(s, t))
    # print(datetime.datetime.now())
    apple = collections.Counter(s)
    orange = collections.Counter(t)
    print(apple.items())
    a = dict()
    print(type(a))
