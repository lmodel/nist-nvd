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
  One entry of a change-history response, which only wraps the change.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NvdChangeItem  {

  private NvdChange change;


}