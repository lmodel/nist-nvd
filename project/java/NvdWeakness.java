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
  The weaknesses that one source says lie behind a vulnerability.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NvdWeakness  {

  private String source;
  private String type;
  private List<NvdLangString> description;


}