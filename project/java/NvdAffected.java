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
  The products that one source says the vulnerability affects.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NvdAffected  {

  private String source;
  private List<NvdAffectedProduct> affectedData;


}