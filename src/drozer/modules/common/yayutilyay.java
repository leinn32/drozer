import java.util.Set;
import android.os.Bundle;

public class yayutilyay {

    public String bundleToString(Bundle yaybundleyay) {
        String yayreturnyay = "";
        Set<String> yaysetyay = yaybundleyay.keySet();
        for (String yaykeyyay : yaysetyay) {
            Object yayvalueyay = yaybundleyay.get(yaykeyyay);
            yayreturnyay = yayreturnyay + yaykeyyay + "=" + yayvalueyay + "(" + yayvalueyay.getClass() + ")\n";
        }

        return yayreturnyay;
    }
}