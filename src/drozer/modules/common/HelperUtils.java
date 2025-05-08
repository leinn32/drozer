import java.util.Set;
import android.os.Bundle;

public class HelperUtils {

    public String bundleToString(Bundle yaybundleyay) {
        String returnString = "";
        Set<String> setString = yaybundleyay.keySet();
        for (String stringKey : setString) {
            Object objectValue = yaybundleyay.get(stringKey);
            returnString = returnString + stringKey + "=" + objectValue + "(" + objectValue.getClass() + ")\n";
        }

        return returnString;
    }
}