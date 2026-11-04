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
  One answer on the way through a decision tree, keyed by its decision point.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NvdSsvcOption  {

  private String exploitation;
  private String automatable;
  private String technicalImpact;


}