package util;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by miller on 2017/8/5 0005.
 */
public class ReadCSVUtil {

    public static List<String> readCSV(String filepath){
        File csv = new File(filepath);  // CSV文件路径
        BufferedReader br = null;
        try {
            br = new BufferedReader(new FileReader(csv));
        }catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        String line = "";
        List<String> allString = new ArrayList<String>();
        try {

            while ((line = br.readLine()) != null)
            {
                allString.add(line);
            }

            System.out.println("csv表格中所有行数："+allString.size());
        } catch (IOException e) {
            e.printStackTrace();
        }

        return allString;
    }
}
