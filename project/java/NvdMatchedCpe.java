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
  A CPE name that a match string matches.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NvdMatchedCpe  {

  private String cpeName;
  private String cpeNameId;


}