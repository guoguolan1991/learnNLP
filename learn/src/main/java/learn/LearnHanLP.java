package learn;

import com.hankcs.hanlp.HanLP;
import com.hankcs.hanlp.seg.common.Term;
import com.hankcs.hanlp.tokenizer.StandardTokenizer;

import java.util.List;

/**
 * Created by Miller on 2017/8/4 0004.
 */
public class LearnHanLP {
    public static void main(String[] args){
        System.out.println(HanLP.segment("开始hanlp分词尝试"));

        List<Term> termList = StandardTokenizer.segment("商品和服务");
        System.out.println(termList);
    }

}
