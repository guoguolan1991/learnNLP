package learn;

import com.hankcs.hanlp.HanLP;
import util.ReadCSVUtil;

import java.util.List;

/**
 * Created by Miller on 2017/8/5 0005.
 */
public class DoubanDemo {
    public static void main(String[] args){
        String filepath = "D:\\workspace\\ML\\learnNLP\\learn\\src\\main\\resources\\douban_zhanlang.csv";
        List<String> strList = ReadCSVUtil.readCSV(filepath);
        StringBuffer stringBuffer = new StringBuffer();

        int len = 0;
        String temp = "";
        String text = "";
        while(len < strList.size()){
            temp = strList.get(len).split(",")[3];
            text += temp;
        }

        List<String> keyWordList = HanLP.extractKeyword(text, 100);
    }
}
