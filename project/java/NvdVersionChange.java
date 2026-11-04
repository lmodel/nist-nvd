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
  A point within a range of versions where the status changes.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NvdVersionChange  {

  private String at;
  private String status;


}