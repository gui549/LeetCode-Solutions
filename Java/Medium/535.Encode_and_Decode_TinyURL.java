package Medium;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

// advanced solution
class Codec {
    
    static final String HOST_URL = "http://tinyurl.com/";
    private static final String charSet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
    private Map<String, String> url2code = new HashMap<>();
    private Map<String, String> code2url = new HashMap<>();

    // Encodes a URL to a shortened URL.
    public String encode(String longUrl) {
        if(longUrl == null || longUrl.isEmpty()) 
            return null;

        if (url2code.containsKey(longUrl))
            return url2code.get(longUrl);

        StringBuilder code = null;
        do {
            code = new StringBuilder();
            for (int i = 0; i < 6; i++) {
                int randomIdx = (int) (Math.random() * charSet.length());
                code.append(charSet.charAt(randomIdx));
            }
        } while (code2url.containsKey(code.toString()));

        url2code.put(longUrl, code.toString());
        code2url.put(code.toString(), longUrl);

        return HOST_URL + code;
    }

    // Decodes a shortened URL to its original URL.
    public String decode(String shortUrl) {
        if (shortUrl == null || shortUrl.isEmpty())
            return null;

        String code = shortUrl.substring(shortUrl.lastIndexOf("/") + 1);
        return code2url.get(code);
    }
}


// simple solution
// class Codec {
//     List<String> urls = new ArrayList<>();

//     // Encodes a URL to a shortened URL.
//     public String encode(String longUrl) {
//         urls.add(longUrl);
//         return "http://tinyurl.com/" + (urls.size() - 1);
//     }

//     // Decodes a shortened URL to its original URL.
//     public String decode(String shortUrl) {
//         return urls.get(Integer.parseInt(shortUrl.substring(shortUrl.lastIndexOf("/") + 1)));
//     }
// }