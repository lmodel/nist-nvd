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
  A page about a vulnerability, with NVD's labels for what it is.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NvdReference  {

  private URI url;
  private String source;
  private List<String> tags;


}