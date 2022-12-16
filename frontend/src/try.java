import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;

import java.io.FileWriter;
import java.io.IOException;

public class Test {
    public static void main(String[] args) throws IOException {
        String url = "http://www.hljkjt.gov.cn/html/zwgk/tztg/list.html";
        String filePath = "C:\\Users\\Administrator\\Desktop\\crawler.txt";
        String ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36";
        Test t = new Test();
        t.getRes(url,filePath,ua);
    }

    public void getRes(String url,String filePath,String ua) throws IOException{
        //解析html
        Document doc = Jsoup.connect(url).timeout(5000).userAgent(ua).get();
        Elements listDiv = doc.getElementsByAttributeValue("class", "List_title");
        String h4 = "";
        String title = "";
        String href = "";
        String res = "";
        for (int i =0;i<listDiv.size();i++) {
            Elements listDivs = doc.getElementsByAttributeValue("class", "listn_box");
            h4 = listDivs.get(i).getElementsByTag("h4")+"\n";

            Elements a = listDiv.get(i).getElementsByTag("a");
            for(int j =0;j<a.size();j++){
                title = a.get(j).attr("title");
                href = a.get(j).attr("href");
                if(j == 0) {
                    res = h4 + "title:" + title + "\thref:http://www.hljkjt.gov.cn" + href + "\n";
                }else {
                    res = "title:" + title + "\thref:http://www.hljkjt.gov.cn" + href + "\n";
                }
                System.out.print(res);
                Test.saveAsFileWriter(res,filePath);
            }
        }

    }
    private static void saveAsFileWriter(String content,String filePath) {
        FileWriter fwriter = null;
        try {
            // true表示不覆盖原来的内容，而是加到文件的后面。若要覆盖原来的内容，直接省略这个参数就好
            fwriter = new FileWriter(filePath, true);
            fwriter.write(content);
        } catch (IOException ex) {
            ex.printStackTrace();
        } finally {
            try {
                fwriter.flush();
                fwriter.close();
            } catch (IOException ex) {
                ex.printStackTrace();
            }
        }
    }
}
