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
  The labels that one source puts on a record.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NvdCveTag  {

  private String sourceIdentifier;
  private List<String> tags;


}