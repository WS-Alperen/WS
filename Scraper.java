import org.jsoup.*;
import org.jsoup.examples.*;
import org.jsoup.helper.*;
import org.jsoup.internal.*;
import org.jsoup.nodes.*;
import org.jsoup.parser.*;
import org.jsoup.safety.*;
import org.jsoup.select.*;
import java.util.*;
import java.io.*;

public class Scraper {

	public static void main(String[] args) 
			throws IOException{
		
		FileWriter f = new FileWriter("GermanFoodBanksInfo.csv");
		
		String base_URL = "http://www.tafel.de/nc/die-tafeln/tafel-suche/adressenliste.html?tx_brtafel_pi1%5Btest%5D=test&tx_brtafel_pi1%5Bpointer%5D=";
		for(int pageNumber = 0; pageNumber <= 38; pageNumber++) {
			Document page = Jsoup.connect(base_URL + pageNumber).get();
			Element foodBankList = page.getElementsByClass("tafel-liste").get(0);
			Elements names = foodBankList.getElementsByTag("dt");
			Elements info = foodBankList.getElementsByTag("dd");
	
			for(int index = 0; index < names.size(); index++) {
				Scanner in = new Scanner(info.get(index).text());
				String address = "";
				String token = in.next();
				while(!(token.equals("Bundesland:") || token.equals("Ansprechpartner:"))) {
					address += token + " ";
					token = in.next();
				}
				
				String mail = "";
				if(info.get(index).select("span").size() != 0) {
					info.get(index).select("span").first().html("");
					mail = info.get(index).select("a").first().text();
				}
				
				String website = "";
				if(info.get(index).select("a[title]").size() != 0) {
					website = info.get(index).select("a[title]").first().text();
				}
				
				f.append("\"" + names.get(index).text() + "\"");
				f.append(",");
				f.append("\"" + address + "\"");
				f.append(",");
				f.append("\"" + mail + "\"");
				f.append(",");
				f.append("\"" + website + "\"");
				f.append("\n");
				f.flush();
				
			}
		}
	}
}
