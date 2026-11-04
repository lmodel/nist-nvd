package example;

/* metamodel_version: 1.12.0 */
/* version: 2.2.4 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A product's title in one language.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NvdCpeTitle  {

  private String title;
  private String lang;


}