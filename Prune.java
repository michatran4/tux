import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Prune {
    public static void main(String[] args) throws IOException {
        File f = new File("in.txt");
        Scanner s = new Scanner(f);
        String text = "";
        while (s.hasNextLine()) {
			String line = s.nextLine();
			line = line.replaceAll("<li>", "- ");
			line = line.replaceAll("</li>", "");
			line = line.replaceAll("<b>", "**");
			line = line.replaceAll("</b>", "**");
			line = line.replaceAll("<i>", "*");
			line = line.replaceAll("</i>", "*");
			line = line.replaceAll("<h1>", "# ");
			line = line.replaceAll("</h1>", "");
			line = line.replaceAll("<h2>", "\n## ");
			line = line.replaceAll("</h2>", "");
			line = line.replaceAll("<ul>", "");
			line = line.replaceAll("</ul>", "");
			line = line.replaceAll("</main>", "\n");
			line = line.replaceAll("<p>", "");
			line = line.replaceAll("</p>", "");
			if (!line.equals("")) {
				text += line + "\n";
			}
        }
		s.close();
        FileWriter fileWriter = new FileWriter("out.txt");
        fileWriter.write(text);
        fileWriter.close();
    }
}
