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
  One part of a change, naming what kind of data changed and how.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NvdChangeDetail  {

  private String type;
  private String action;
  private String oldValue;
  private String newValue;


}