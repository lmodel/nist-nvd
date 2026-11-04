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
  One entry of a match-string response, which only wraps the match string.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NvdMatchStringItem  {

  private NvdMatchString matchString;


}